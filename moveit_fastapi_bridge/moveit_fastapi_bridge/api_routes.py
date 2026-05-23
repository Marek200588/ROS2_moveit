from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel

router = APIRouter()
class JointCommand(BaseModel):
    joint_names:list[str]
    joint_positions:list[float]
    duration:float
@router.post("/move_arm/joints")
async def move_joints(command: JointCommand, request: Request):
    ros_node = request.app.state.ros_node
    if len(command.joint_names) != len(command.joint_positions):
        raise HTTPException(status_code=400, detail="there should be as many moveable joints as we want to move")
    success = ros_node.move_joints(command.joint_names, command.joint_positions, command.duration)
    if success:
        return { "status" : "success" , "message" : "the arm is moving to the desired position"}
    else:
        raise HTTPException(status_code=500, detail="something went wrong while trying to move the arm")
@router.get("/arm/status")
async def get_arm_status(request: Request):
    ros_node = request.app.state.ros_node
    if not ros_node.current_joints:
        raise HTTPException(status_code=503, detail="joint state information is not available yet")
    return { "status" : "success", "current_joints" : ros_node.current_joints }