import React, { useState } from 'react'

export default function App() {
  const [checklist, setchecklist] = useState('')
  const [variables, setVariables] = useState([{ key: '', value: '' }])
  const [pageLocators, setPageLocators] = useState([{ key: '', value: '' }])
  const [aiProvider, setAiProvider] = useState('mistral')
  const [masking, setMasking] = useState('simple')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)

  const addVariable = () => {
    setVariables([...variables, { key: '', value: '' }])
  }

  const removeVariable = (index) => {
    setVariables(variables.filter((_, i) => i !== index))
  }

  const addPageLocator = () => {
    setPageLocators([...pageLocators, { key: '', value: '' }])
  }

  const removePageLocator = (index) => {
    setPageLocators(pageLocators.filter((_, i) => i !== index))
  }

  const updateVariable = (index, field, value) => {
    const updated = [...variables]
    updated[index][field] = value
    setVariables(updated)
  }

  const updatePageLocator = (index, field, value) => {
    const updated = [...pageLocators]
    updated[index][field] = value
    setPageLocators(updated)
  }

  const runPipeline = async () => {
    setLoading(true)
    setResult(null)

    const vars = {}
    variables.forEach(v => {
      if (v.key) vars[v.key] = v.value
    })

    const locators = {}
    pageLocators.forEach(p => {
      if (p.key) locators[p.key] = p.value
    })

    const payload = {
      checklist: { content: checklist },
      variables: vars,
      page_locators: locators,
      config: {
        aiProvider,
        piiMasking: { mode: masking }
      }
    }

    const res = await fetch("http://localhost:3000/pipeline/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    })

    const data = await res.json()
    setResult(data)
    setLoading(false)
  }

  return (
    <div className="container">
      <h1>QA Automation Pipeline</h1>

      <div className="card">
        <h3>Checklist Input</h3>
        <textarea
          rows={5}
          value={checklist}
          onChange={e => setchecklist(e.target.value)}
        />
      </div>

      <div className="card">
        <h3>Test Variables</h3>
        {variables.map((v, i) => (
          <div className="row" key={i}>
            <input
              placeholder="Key"
              value={v.key}
              onChange={e => updateVariable(i, 'key', e.target.value)}
            />
            <input
              placeholder="Value"
              value={v.value}
              onChange={e => updateVariable(i, 'value', e.target.value)}
            />
            <button className="danger" onClick={() => removeVariable(i)}>X</button>
          </div>
        ))}
        <button onClick={addVariable}>+ Add Variable</button>
      </div>

      <div className="card">
        <h3>Page Locators</h3>
        {pageLocators.map((p, i) => (
          <div className="row" key={i}>
            <input
              placeholder="Key"
              value={p.key}
              onChange={e => updatePageLocator(i, 'key', e.target.value)}
            />
            <input
              placeholder="Value"
              value={p.value}
              onChange={e => updatePageLocator(i, 'value', e.target.value)}
            />
            <button className="danger" onClick={() => removePageLocator(i)}>X</button>
          </div>
        ))}
        <button onClick={addPageLocator}>+ Add Page Locator</button>
      </div>

      <div className="card">
        <h3>Configuration</h3>
        <label>AI Provider</label>
        <select value={aiProvider} onChange={e => setAiProvider(e.target.value)}>
          <option value="mistral">Mistral</option>
          <option value="gemini">Gemini</option>
        </select>

        <label>PII Masking</label>
        <select value={masking} onChange={e => setMasking(e.target.value)}>
          <option value="simple">Simple</option>
          <option value="ai">AI</option>
        </select>
      </div>

      <button className="primary" onClick={runPipeline}>
        {loading ? "Running..." : "Run Pipeline"}
      </button>

      {result && (
        <div className="card">
          <h3>Results</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  )
}
