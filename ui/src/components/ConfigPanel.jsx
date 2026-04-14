import React from 'react'

export default function ConfigPanel({ aiProvider, setAiProvider, masking, setMasking }) {
  return (
    <div className="card">
      <h3>Configuration</h3>
      <div className="form-group">
        <label>AI Provider</label>
        <select value={aiProvider} onChange={e => setAiProvider(e.target.value)}>
          <option value="mistral">Mistral</option>
          <option value="gemini">Gemini</option>
        </select>
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
