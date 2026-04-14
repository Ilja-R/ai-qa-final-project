import React from 'react'

export default function DynamicList({ title, items, onChange, onAdd, onRemove }) {
  return (
    <div className="card">
      <h3>{title}</h3>
      {items.map((item, i) => (
        <div className="row" key={i}>
          <input
            placeholder="Key"
            value={item.key}
            onChange={e => onChange(i, 'key', e.target.value)}
          />
          <input
            placeholder="Value"
            value={item.value}
            onChange={e => onChange(i, 'value', e.target.value)}
          />
          <button className="danger" onClick={() => onRemove(i)}>X</button>
        </div>
      ))}
      <button onClick={onAdd}>+ Add {title.slice(0, -1)}</button>
    </div>
  )
}
