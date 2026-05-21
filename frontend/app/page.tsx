"use client";

import { useState } from "react";

export default function Home() {
  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");

  return (
    <main className="min-h-screen p-10">
      <h1 className="text-4xl font-bold mb-8">
        AI Resume Matcher
      </h1>

      <div className="flex flex-col gap-6 max-w-2xl">

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
          className="border p-3 rounded h-60"
          onChange={(e) => setJobDescription(e.target.value)}
        />

        <button className="bg-black text-white p-3 rounded">
          Analyze Resume
        </button>

      </div>
    </main>
  );
}