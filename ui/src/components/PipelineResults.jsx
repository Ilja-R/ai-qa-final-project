import React, { useState } from 'react'

const TabButton = ({ active, onClick, label, id }) => (
  <button
    className={`tab-btn ${active ? 'active' : ''}`}
    onClick={() => onClick(id)}
  >
    {label}
  </button>
)

export default function PipelineResults({ result }) {
  const [activeTab, setActiveTab] = useState('scenarios')

  if (!result) return null

  const renderScenarios = () => {
    const scenarios = result.scenarios || []
    if (scenarios.length === 0) return <p>No scenarios generated.</p>

    return (
      <div className="scenarios-list">
        {scenarios.map((scenario, idx) => (
          <div key={idx} className="scenario-item card">
            <h4>{scenario.name}</h4>
            <table className="data-table">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Step</th>
                  <th>Expected Result</th>
                </tr>
              </thead>
              <tbody>
                {scenario.steps.map((step, sIdx) => (
                  <tr key={sIdx}>
                    <td>{sIdx + 1}</td>
                    <td>{step.step}</td>
                    <td>{step.expected}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ))}
      </div>
    )
  }

  const renderCode = () => {
    const files = result.generated_code || []
    if (files.length === 0) return <p>No code generated.</p>

    return (
      <div className="code-files">
        {files.map((file, idx) => (
          <div key={idx} className="code-file-item">
            <div className="file-header">
              <strong>{file.path}</strong>
            </div>
            <pre className="code-block">
              <code>{file.content}</code>
            </pre>
          </div>
        ))}
      </div>
    )
  }

  const renderReview = () => {
    if (!result.code_review) return <p>No review available.</p>
    const review = result.code_review
    
    return (
      <div className="review-content card">
        <div className="review-header">
          <h3>Overall Score</h3>
          <div className="score-badge big-score">{review.overall_score}/100</div>
        </div>

        <div className="review-section">
          <h3>Part 1: Summary</h3>
          <p>{review.summary}</p>
        </div>
        
        <div className="review-section">
          <h3>Part 2: Critical Issues</h3>
          {review.critical_issues && review.critical_issues.length > 0 ? (
            <ul className="critical-list">
              {review.critical_issues.map((issue, i) => (
                <li key={i} className="critical-item">
                  <strong>{issue.file}:{issue.line}</strong> - {issue.issue}
                  <div className="suggestion-text">Fix: {issue.suggestion}</div>
                </li>
              ))}
            </ul>
          ) : (
            <p>No critical issues found.</p>
          )}
        </div>
        
        <div className="review-section">
          <h3>Part 3: Suggestions</h3>
          {review.suggestions && review.suggestions.length > 0 ? (
            <table className="data-table">
              <thead>
                <tr>
                  <th>File</th>
                  <th>Line</th>
                  <th>Issue</th>
                  <th>Suggestion</th>
                </tr>
              </thead>
              <tbody>
                {review.suggestions.map((s, i) => (
                  <tr key={i}>
                    <td>{s.file}</td>
                    <td>{s.line}</td>
                    <td>{s.issue}</td>
                    <td>{s.suggestion}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : (
            <p>No suggestions.</p>
          )}
        </div>

        <div className="review-section">
          <h3>Part 4: Possible Observations</h3>
          {review.positive_observations && review.positive_observations.length > 0 ? (
            <table className="data-table">
              <thead>
                <tr>
                  <th>Observation</th>
                </tr>
              </thead>
              <tbody>
                {review.positive_observations.map((obs, i) => (
                  <tr key={i}>
                    <td>{obs}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : (
            <p>No observations.</p>
          )}
        </div>
      </div>
    )
  }

  const renderBugReport = () => {
    if (!result.bug_report) return <p>No bug report available.</p>
    const bug = result.bug_report
    
    return (
      <div className="bug-report-content card">
        <h4>AI Generated Bug Report</h4>
        <div className={`status-badge ${bug.status === 'SUCCESS' ? 'success' : 'error'}`}>
          Status: {bug.status}
        </div>
        
        <div className="form-group" style={{ marginTop: '1rem' }}>
          <pre style={{ whiteSpace: 'pre-wrap', background: '#f8fafc', color: '#1e293b', padding: '1rem', border: '1px solid #e2e8f0' }}>
            {bug.report || bug.raw || JSON.stringify(bug, null, 2)}
          </pre>
        </div>
      </div>
    )
  }

  const renderMasking = () => {
    if (!result.masking) return <p>No masking data.</p>
    return (
      <div className="masking-info card">
        <div className="form-group">
          <label>Masked Text</label>
          <pre>{result.masking.masked_text}</pre>
        </div>
        {result.masking.entities && result.masking.entities.length > 0 && (
          <div className="form-group">
            <label>Detected Entities</label>
            <table className="data-table">
              <thead>
                <tr>
                  <th>Type</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                {result.masking.entities.map((ent, idx) => (
                  <tr key={idx}>
                    <td>{ent.label}</td>
                    <td>{ent.text}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    )
  }

  return (
    <div className="pipeline-results">
      <div className="results-header">
        <h3>Pipeline Results {result.run_id && <small>(Run: {result.run_id})</small>}</h3>
        <div className="tabs">
          <TabButton id="masking" label="1. Masking" active={activeTab === 'masking'} onClick={setActiveTab} />
          <TabButton id="scenarios" label="2. Scenarios" active={activeTab === 'scenarios'} onClick={setActiveTab} />
          <TabButton id="code" label="3. Code" active={activeTab === 'code'} onClick={setActiveTab} />
          <TabButton id="review" label="4. Review" active={activeTab === 'review'} onClick={setActiveTab} />
          <TabButton id="bug_report" label="5. Bug Report" active={activeTab === 'bug_report'} onClick={setActiveTab} />
        </div>
      </div>

      <div className="tab-content">
        {activeTab === 'masking' && renderMasking()}
        {activeTab === 'scenarios' && renderScenarios()}
        {activeTab === 'code' && renderCode()}
        {activeTab === 'review' && renderReview()}
        {activeTab === 'bug_report' && renderBugReport()}
      </div>
    </div>
  )
}
