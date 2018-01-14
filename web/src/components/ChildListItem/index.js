import React from 'react';

type Props = {
  child: {
    id: number,
    name: string,
  },
  currentChildIds: Array,
  // onRoomJoin: () => void,
}

const ChildListItem = ({ child, currentChildId }: Props) => {
  // const isJoined = currentChildIds.includes(child.id);

  return (
    <div key={child.id} style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '10px' }}>
      <span style={{ marginRight: '8px' }}>{child.name}</span>
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

export default ChildListItem;
