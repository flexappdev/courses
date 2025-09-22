import { useEffect, useMemo, useState } from "react";

const DEFAULT_API = "http://localhost:2049";

function useApiBase() {
  return useMemo(() => {
    const base = import.meta.env.VITE_API_URL || DEFAULT_API;
    return base.replace(/\/$/, "");
  }, []);
}

function CourseList({ courses, onSelect, selectedId }) {
  if (!courses.length) {
    return <p className="empty">No courses available yet.</p>;
  }

  return (
    <ul className="course-list">
      {courses.map((course) => (
        <li key={course.id} className={course.id === selectedId ? "active" : ""}>
          <button type="button" onClick={() => onSelect(course)}>
            <span className="title">{course.title}</span>
            {course.tagline && <span className="tagline">{course.tagline}</span>}
            {course.topics?.length ? (
              <span className="topics">{course.topics.length} topics</span>
            ) : null}
          </button>
        </li>
      ))}
    </ul>
  );
}

function CourseDetail({ course }) {
  if (!course) {
    return (
      <div className="course-detail placeholder">
        <h2>Select a course</h2>
        <p>
          Choose a course from the list to review its eight sessions, supporting materials, and
          presentation-ready slide notes.
        </p>
      </div>
    );
  }

  return (
    <div className="course-detail">
      <header>
        <h2>{course.title}</h2>
        {course.metadata.tagline && <p className="tagline">{course.metadata.tagline}</p>}
        {course.metadata.description && <p className="description">{course.metadata.description}</p>}
      </header>
      {course.sessions.length ? (
        <section>
          <h3>Session overview</h3>
          <ol>
            {course.sessions.map((session) => (
              <li key={session.id}>
                <h4>{session.title || session.name}</h4>
                {session.tagline && <p className="tagline">{session.tagline}</p>}
                {session.keyIdeas?.length ? (
                  <ul className="key-ideas">
                    {session.keyIdeas.map((idea, index) => (
                      <li key={index}>{idea}</li>
                    ))}
                  </ul>
                ) : null}
              </li>
            ))}
          </ol>
        </section>
      ) : (
        <p>This course does not include any detailed sessions yet.</p>
      )}
    </div>
  );
}

export default function App() {
  const apiBase = useApiBase();
  const [courses, setCourses] = useState([]);
  const [selectedCourse, setSelectedCourse] = useState(null);
  const [selectedId, setSelectedId] = useState(null);
  const [loading, setLoading] = useState(true);
  const [detailLoading, setDetailLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadCourses() {
      setLoading(true);
      setError(null);
      try {
        const response = await fetch(`${apiBase}/courses`);
        if (!response.ok) {
          throw new Error(`API responded with status ${response.status}`);
        }
        const payload = await response.json();
        setCourses(payload);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    loadCourses();
  }, [apiBase]);

  async function handleSelect(course) {
    setSelectedId(course.id);
    setDetailLoading(true);
    setError(null);
    try {
      const response = await fetch(`${apiBase}/courses/${course.slug || course.id}`);
      if (!response.ok) {
        throw new Error(`Failed to load course ${course.id}`);
      }
      const payload = await response.json();
      setSelectedCourse(payload);
    } catch (err) {
      setError(err.message);
    } finally {
      setDetailLoading(false);
    }
  }

  return (
    <div className="app-shell">
      <aside>
        <div className="panel">
          <h1>English Teacher</h1>
          <p className="intro">
            Browse the library of business-focused English courses. Every syllabus follows an eight-session
            flow with presentation-ready content.
          </p>
        </div>
        <div className="panel list">
          <div className="panel-header">
            <h2>Courses</h2>
            {loading && <span className="status">Loading…</span>}
          </div>
          {error && <p className="error">{error}</p>}
          {!loading && !error && (
            <CourseList courses={courses} onSelect={handleSelect} selectedId={selectedId} />
          )}
        </div>
      </aside>
      <main>
        {detailLoading && <p className="status">Loading course details…</p>}
        {!detailLoading && !error && <CourseDetail course={selectedCourse} />}
        {!detailLoading && error && <p className="error">{error}</p>}
      </main>
    </div>
  );
}
