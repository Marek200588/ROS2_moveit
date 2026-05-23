import rclpy
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
import threading

from moveit_fastapi_bridge.moveit_node import MoveItSceneNode
from moveit_fastapi_bridge.api_routes import router
@asynccontextmanager 
async def lifespan(app: FastAPI):
    # --- STARTUP ---
    rclpy.init()
    ros_node = MoveItSceneNode()
    app.state.ros_node = ros_node
    
    # Przypisujemy do zwykłej zmiennej zamiast do atrybutu węzła
    ros_thread = threading.Thread(target=rclpy.spin, args=(ros_node,), daemon=True)
    ros_thread.start()
    
    # Serwer w tym miejscu przejmuje kontrole i nasłuchuje zapytań HTTP
    yield
    
    # --- SHUTDOWN --- (Kolejność jest krytyczna!)
    rclpy.shutdown()          # 1. Wyłączamy kontekst ROS 2 (zatrzymuje to rclpy.spin)
    ros_thread.join()         # 2. Czekamy, aż wątek się faktycznie zakończy
    ros_node.destroy_node()   # 3. Teraz bezpiecznie niszczymy węzeł
instance = FastAPI(lifespan=lifespan, docs_url="/")
instance.include_router(router)
def main():
    uvicorn.run(instance, host="0.0.0.0", port= 8000)

if __name__ == "__main__":
    main()

