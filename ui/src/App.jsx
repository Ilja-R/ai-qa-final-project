import React, { useState } from 'react'
import DynamicList from './components/DynamicList'
import ConfigPanel from './components/ConfigPanel'

export default function App() {
  const [checklist, setChecklist] = useState('')
  const [variables, setVariables] = useState([{ key: '', value: '' }])
  const [pageLocators, setPageLocators] = useState([{ key: '', value: '' }])
  const [aiProvider, setAiProvider] = useState('mistral')
  const [masking, setMasking] = useState('simple')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleUpdateItem = (list, setList, index, field, value) => {
    const updated = [...list]
    updated[index][field] = value
    setList(updated)
  }

  const handleAddItem = (list, setList) => {
    setList([...list, { key: '', value: '' }])
  }

  const handleRemoveItem = (list, setList, index) => {
    setList(list.filter((_, i) => i !== index))
  }

  const runPipeline = async () => {
    setLoading(true)
    setResult(null)
    setError(null)

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
      provider: aiProvider,
      config: {
        piiMasking: { mode: masking }
      }
    }

    try {
      const res = await fetch("http://localhost:3000/pipeline/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      })

      if (!res.ok) {
        throw new Error(`API error: ${res.status} ${res.statusText}`)
      }

      const data = await res.json()
      setResult(data)
    } catch (err) {
      console.error(err)
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <header>
        <h1>AI QA Automation Pipeline</h1>
        <p>Generate test scenarios, code, and bug reports from your checklists.</p>
      </header>

      <main>
        <div className="card">
          <h3>Checklist Input</h3>
          <textarea
            placeholder="Enter your testing requirements/checklist here..."
            rows={8}
            value={checklist}
            onChange={e => setChecklist(e.target.value)}
          />
        </div>

        <div className="grid">
          <DynamicList
            title="Variables"
            items={variables}
            onChange={(idx, f, v) => handleUpdateItem(variables, setVariables, idx, f, v)}
            onAdd={() => handleAddItem(variables, setVariables)}
            onRemove={(idx) => handleRemoveItem(variables, setVariables, idx)}
          />

          <DynamicList
            title="Page Locators"
            items={pageLocators}
            onChange={(idx, f, v) => handleUpdateItem(pageLocators, setPageLocators, idx, f, v)}
            onAdd={() => handleAddItem(pageLocators, setPageLocators)}
            onRemove={(idx) => handleRemoveItem(pageLocators, setPageLocators, idx)}
          />
        </div>

        <ConfigPanel
          aiProvider={aiProvider}
          setAiProvider={setAiProvider}
          masking={masking}
          setMasking={setMasking}
        />

        <div className="actions">
          <button className="primary big" onClick={runPipeline} disabled={loading || !checklist}>
            {loading ? "Processing Pipeline..." : "🚀 Run Full E2E Pipeline"}
          </button>
        </div>

        {error && (
          <div className="card error">
            <h3>Error</h3>
            <p>{error}</p>
          </div>
        )}

        {result && (
          <div className="card result-container">
            <h3>Pipeline Results</h3>
            <div className="result-tabs">
              <pre>{JSON.stringify(result, null, 2)}</pre>
            </div>
          </div>
        )}
      </main>
    </div>
  )
}
