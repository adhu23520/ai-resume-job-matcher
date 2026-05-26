"use client";

import { useState } from "react";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!file || !jobDescription) {
      alert("Please upload a resume and paste a job description.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_description", jobDescription);

    setLoading(true);

    try {
      const response = await fetch("http://localhost:8000/match", {
        method: "POST",
        body: formData,
      });

      console.log("Response status:", response.status);

      const data = await response.json();
      console.log("Backend response:", data);

      if (!response.ok) {
        throw new Error(data.detail || "Backend error");
      }

      setResult(data);
    } catch (error) {
      console.error("Error:", error);
      alert("Something went wrong while analyzing.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen p-10 bg-black text-white">
      <h1 className="text-5xl font-bold mb-10">
        AI Resume Matcher
      </h1>

      <div className="flex flex-col gap-6 max-w-3xl">

        <input
          type="file"
          className="border p-3 rounded"
          onChange={(e) => {
            if (e.target.files) {
              setFile(e.target.files[0]);
            }
          }}
        />

        <textarea
          placeholder="Paste Job Description Here..."
          className="border p-4 rounded h-72 bg-black"
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
        />

        <button
          onClick={handleAnalyze}
          className="bg-white text-black p-4 rounded font-semibold"
        >
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>

        {result && (
          <div className="border p-6 rounded mt-6">
            <h2 className="text-3xl font-bold mb-4">
              Analysis Result
            </h2>

            <p className="mb-2">
              <strong>Filename:</strong> {result.filename ?? "N/A"}
            </p>

            <p className="mb-2">
              <strong>Match Score:</strong> {result.match_score ?? "N/A"}
            </p>

            <p className="mb-2">
              <strong>Match Level:</strong> {result.match_level ?? "N/A"}
            </p>

            <div className="mt-4">
              <h3 className="text-xl font-semibold mb-2">
                Resume Preview
              </h3>

              <p className="text-sm whitespace-pre-wrap">
                {result.resume_preview ?? ""}
              </p>
            </div>
          </div>
        )}

      </div>
    </main>
  );
}