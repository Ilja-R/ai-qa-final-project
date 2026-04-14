import React from 'react'

export default function ConfigPanel({ aiProvider, setAiProvider, masking, setMasking, availableProviders = [] }) {
  return (
    <div className="card">
      <h3>Configuration</h3>
      <div className="form-group">
        <label>AI Provider</label>
        {availableProviders.length > 0 ? (
          <select value={aiProvider} onChange={e => setAiProvider(e.target.value)}>
            {availableProviders.map(provider => (
              <option key={provider.id} value={provider.id}>
                {provider.name}
              </option>
            ))}
          </select>
        ) : (
          <div className="error-text">No AI providers available. Please set your API keys.</div>
        )}
      </div>

      <div className="form-group">
        <label>PII Masking</label>
        <select value={masking} onChange={e => setMasking(e.target.value)}>
          <option value="simple">Simple</option>
          <option value="ai">AI</option>
        </select>
      </div>
    </div>
  )
}
