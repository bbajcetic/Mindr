import React from 'react';

type Props = {
  camera: {
    id: number,
    name: string,
  },
  currentCameraIds: Array,
  // onRoomJoin: () => void,
}

const CameraListItem = ({ camera, currentCameraId }: Props) => {
  // const isJoined = currentCameraIds.includes(child.id);

  return (
    <div key={camera.id} style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '10px' }}>
      <span style={{ marginRight: '8px' }}>{camera.name}</span>
      {/* <button
        onClick={() => onRoomJoin(room.id)}
        className="btn btn-sm"
        disabled={isJoined}
      >
        {isJoined ? 'Joined' : 'Join'}
      </button> */}
    </div>
  );
};

export default CameraListItem;
