import React, { useState } from "react";
import axios from "axios";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  CartesianGrid,
} from "recharts";
import Table from "react-bootstrap/Table";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

export default function Chatbox() {
  const [query, setQuery] = useState("");
  const [summary, setSummary] = useState("");
  const [chartData, setChartData] = useState({});
  const [tableData, setTableData] = useState([]);
  const [errorMsg, setErrorMsg] = useState("");

  const callApi = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:8000/api/analyze/", {
        query: query,
      });

      // Clear previous error message on success
      setErrorMsg("");
      setSummary(res.data.summary || "");
      setChartData(res.data.charts || {});
      setTableData(res.data.table || []);
    } catch (e) {
      if (e.response?.data?.error) {
        setErrorMsg(e.response.data.error);
      } else {
        setErrorMsg("Something went wrong. Try again.");
      }
      setSummary("");
      setChartData({});
      setTableData([]);
    }
  };

  return (
    <div className="mt-3" style={{ maxWidth: "750px" }}>
      <Form
        onSubmit={(e) => {
          e.preventDefault();
          callApi();
        }}
      >
        <Form.Group className="mb-2">
          <Form.Control
            placeholder="Ask anything (E.g., Compare Wakad and Aundh / Analysis of Akurdi)"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
        </Form.Group>
        <Button type="submit">Analyze</Button>
      </Form>

      {/* Error message */}
      {errorMsg && (
        <div className="mt-3 p-2 border bg-danger text-white rounded">
          {errorMsg}
        </div>
      )}

      {/* Summary */}
      {summary && (
        <div className="mt-4">
          <h5>Summary</h5>
          <div className="p-2 border bg-light">{summary}</div>
        </div>
      )}

      {/* Chart */}
      {Object.keys(chartData).length > 0 && (
        <div className="mt-4">
          <h5>Price & Demand Trend</h5>
          <LineChart width={700} height={350}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis tickFormatter={(v) => `${v} Cr`} />
            <Tooltip />
            <Legend />

            {Object.keys(chartData).map((area, i) => (
              <React.Fragment key={area}>
                <Line
                  type="monotone"
                  data={chartData[area]}
                  dataKey="price"
                  name={`${area} — price`}
                  stroke={["#3366ff", "#ff33aa", "#22aa22", "#ffaa00"][i]}
                />
                <Line
                  type="monotone"
                  data={chartData[area]}
                  dataKey="demand"
                  name={`${area} — demand`}
                  stroke={["#66bbff", "#ff6688", "#44cc44", "#ffcc44"][i]}
                />
              </React.Fragment>
            ))}
          </LineChart>
        </div>
      )}

      {/* Table */}
      {tableData.length > 0 && (
        <div className="mt-4">
          <h5>Filtered Data</h5>
          <Table bordered striped hover>
            <thead>
              <tr>
                <th>Area</th>
                <th>Year</th>
                <th>Total Sales (₹)</th>
                <th>Total Units Sold</th>
                <th>Carpet Area (sqft)</th>
              </tr>
            </thead>
            <tbody>
              {tableData.map((row, i) => (
                <tr key={i}>
                  <td>{row.Area}</td>
                  <td>{row.Year}</td>
                  <td>{row["Total Sales (₹)"]}</td>
                  <td>{row["Total Units Sold"]}</td>
                  <td>{row["Carpet Area (sqft)"]}</td>
                </tr>
              ))}
            </tbody>
          </Table>
        </div>
      )}
    </div>
  );
}
