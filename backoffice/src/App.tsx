import { type FormEvent, useCallback, useEffect, useMemo, useState } from "react";
import { BookOpen, CalendarClock, ExternalLink, ListChecks, RefreshCw, Search } from "lucide-react";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";

const DEFAULT_API = "http://localhost:2049";

interface CourseSummary {
  id: string;
  slug: string;
  title: string;
  description?: string | null;
  tagline?: string | null;
  status?: string | null;
  topics: string[];
  updated?: string | null;
  source: string;
}

interface CourseMetadata {
  id: string;
  slug: string;
  title: string;
  name?: string | null;
  tagline?: string | null;
  description?: string | null;
  status?: string | null;
  category?: string | null;
  cta?: string | null;
  year?: string | null;
  topics: string[];
  updated?: string | null;
  source: string;
}

interface CourseSession {
  id: string;
  title?: string | null;
  name?: string | null;
  tagline?: string | null;
  description?: string | null;
  keyIdeas: string[];
  status?: string | null;
  category?: string | null;
  callToAction?: string | null;
  year?: string | null;
  rank?: number | null;
  image?: string | null;
}

interface CourseDetail extends CourseSummary {
  metadata: CourseMetadata;
  sessions: CourseSession[];
}

function formatDate(value?: string | null) {
  if (!value) return null;
  const parsed = new Date(value);
  if (Number.isNaN(parsed.getTime())) {
    return null;
  }
  return parsed.toLocaleDateString(undefined, {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
}

function useApiBase() {
  return useMemo(() => {
    const base = import.meta.env.VITE_API_URL || DEFAULT_API;
    return String(base).replace(/\/$/, "");
  }, []);
}

export default function App() {
  const apiBase = useApiBase();
  const [courses, setCourses] = useState<CourseSummary[]>([]);
  const [selectedCourse, setSelectedCourse] = useState<CourseDetail | null>(null);
  const [loading, setLoading] = useState(true);
  const [searching, setSearching] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [searchTerm, setSearchTerm] = useState("");

  const loadCourses = useCallback(
    async (query?: string) => {
      setError(null);
      setLoading(!query);
      setSearching(Boolean(query));
      try {
        const url = new URL(`${apiBase}/courses`);
        if (query) {
          url.searchParams.set("search", query);
        }
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`Unable to fetch courses (status ${response.status})`);
        }
        const payload = (await response.json()) as CourseSummary[];
        setCourses(payload);
      } catch (err) {
        setError(err instanceof Error ? err.message : String(err));
        setCourses([]);
      } finally {
        setLoading(false);
        setSearching(false);
      }
    },
    [apiBase]
  );

  const loadCourseDetail = useCallback(
    async (identifier: string) => {
      setError(null);
      try {
        const response = await fetch(`${apiBase}/courses/${identifier}`);
        if (!response.ok) {
          throw new Error(`Course ${identifier} could not be loaded`);
        }
        const payload = (await response.json()) as CourseDetail;
        setSelectedCourse(payload);
      } catch (err) {
        setError(err instanceof Error ? err.message : String(err));
        setSelectedCourse(null);
      }
    },
    [apiBase]
  );

  useEffect(() => {
    loadCourses().catch((err) => {
      console.error(err);
    });
  }, [loadCourses]);

  const handleSearch = useCallback(
    async (event: FormEvent<HTMLFormElement>) => {
      event.preventDefault();
      await loadCourses(searchTerm.trim() || undefined);
    },
    [loadCourses, searchTerm]
  );

  const handleRefresh = useCallback(async () => {
    setSearchTerm("");
    await loadCourses();
  }, [loadCourses]);

  const handleSelect = useCallback(
    async (course: CourseSummary) => {
      await loadCourseDetail(course.slug || course.id);
    },
    [loadCourseDetail]
  );

  return (
    <div className="min-h-screen bg-muted/30">
      <header className="border-b bg-white">
        <div className="container mx-auto flex flex-col gap-4 px-6 py-6 md:flex-row md:items-center md:justify-between">
          <div className="flex items-center gap-4">
            <span className="flex h-12 w-12 items-center justify-center rounded-2xl bg-primary/10 text-primary">
              <BookOpen className="h-6 w-6" aria-hidden="true" />
            </span>
            <div>
              <h1 className="text-2xl font-semibold tracking-tight">English Teacher Backoffice</h1>
              <p className="text-sm text-muted-foreground">
                Monitor JSON-driven course assets and keep eight-session roadmaps aligned.
              </p>
            </div>
          </div>
          <Button variant="outline" onClick={handleRefresh} className="w-full md:w-auto">
            <RefreshCw className="mr-2 h-4 w-4" aria-hidden="true" /> Reload catalogue
          </Button>
        </div>
      </header>

      <main className="container mx-auto grid gap-6 px-6 py-10 lg:grid-cols-[360px_1fr]">
        <Card>
          <CardHeader>
            <CardTitle>Course library</CardTitle>
            <CardDescription>Loaded from the repository&apos;s json/ directory.</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <form onSubmit={handleSearch} className="space-y-3">
              <label className="flex flex-col gap-2 text-sm font-medium text-muted-foreground">
                Search catalogue
                <div className="relative">
                  <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
                  <Input
                    placeholder="Filter by title, description, or topics"
                    className="pl-9"
                    value={searchTerm}
                    onChange={(event) => setSearchTerm(event.target.value)}
                  />
                </div>
              </label>
              <div className="flex gap-2">
                <Button type="submit" className="flex-1" disabled={searching}>
                  {searching ? "Searching…" : "Apply filters"}
                </Button>
                <Button type="button" variant="ghost" onClick={handleRefresh}>
                  Reset
                </Button>
              </div>
            </form>
            <div className="space-y-2">
              {loading ? (
                <p className="text-sm text-muted-foreground">Loading courses…</p>
              ) : error ? (
                <p className="text-sm text-destructive">{error}</p>
              ) : courses.length === 0 ? (
                <p className="text-sm text-muted-foreground">No courses match the current filters.</p>
              ) : (
                <ul className="space-y-2">
                  {courses.map((course) => (
                    <li key={course.id}>
                      <button
                        type="button"
                        onClick={() => handleSelect(course)}
                        className="w-full rounded-xl border border-border bg-white px-4 py-3 text-left shadow-sm transition hover:border-primary/40 hover:bg-primary/5"
                      >
                        <div className="flex items-start justify-between gap-3">
                          <div>
                            <p className="font-semibold text-foreground">{course.title}</p>
                            {course.tagline && (
                              <p className="text-xs text-muted-foreground">{course.tagline}</p>
                            )}
                          </div>
                          {course.status && (
                            <span className="rounded-full bg-secondary px-3 py-0.5 text-xs font-medium text-secondary-foreground">
                              {course.status}
                            </span>
                          )}
                        </div>
                        {course.topics?.length ? (
                          <p className="mt-2 line-clamp-2 text-xs text-muted-foreground">
                            Topics: {course.topics.join(", ")}
                          </p>
                        ) : null}
                        {formatDate(course.updated) && (
                          <p className="mt-1 flex items-center gap-1 text-[11px] uppercase tracking-wide text-muted-foreground">
                            <CalendarClock className="h-3.5 w-3.5" /> Updated {formatDate(course.updated)}
                          </p>
                        )}
                      </button>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </CardContent>
        </Card>

        <DetailPanel course={selectedCourse} error={error} />
      </main>
    </div>
  );
}

function DetailPanel({ course, error }: { course: CourseDetail | null; error: string | null }) {
  if (error && !course) {
    return (
      <Card className="border-destructive/40 bg-destructive/5">
        <CardHeader>
          <CardTitle className="text-destructive">Unable to load course</CardTitle>
          <CardDescription className="text-destructive">{error}</CardDescription>
        </CardHeader>
      </Card>
    );
  }

  if (!course) {
    return (
      <Card className="flex h-full flex-col items-center justify-center border-dashed text-center text-muted-foreground">
        <ListChecks className="mb-4 h-12 w-12" aria-hidden="true" />
        <CardTitle className="text-lg">Select a course to inspect its sessions</CardTitle>
        <CardDescription className="px-10">
          Use the library panel to review JSON metadata, session objectives, and slide-ready bullet points
          for each eight-session programme.
        </CardDescription>
      </Card>
    );
  }

  const updatedLabel = formatDate(course.metadata.updated);

  return (
    <Card className="h-full">
      <CardHeader className="space-y-3">
        <div className="space-y-1">
          <CardTitle>{course.title}</CardTitle>
          {course.tagline && <CardDescription>{course.tagline}</CardDescription>}
        </div>
        <div className="grid gap-3 text-sm text-muted-foreground">
          {course.metadata.description && <p>{course.metadata.description}</p>}
          <div className="flex flex-wrap gap-2">
            {course.metadata.topics.map((topic) => (
              <span
                key={topic}
                className="rounded-full bg-primary/10 px-3 py-1 text-xs font-medium text-primary"
              >
                {topic}
              </span>
            ))}
          </div>
          <dl className="grid grid-cols-[auto_1fr] gap-x-3 gap-y-1 text-xs uppercase tracking-wide text-muted-foreground/90">
            {course.metadata.status && (
              <>
                <dt>Status</dt>
                <dd className="font-medium text-foreground">{course.metadata.status}</dd>
              </>
            )}
            {course.metadata.category && (
              <>
                <dt>Category</dt>
                <dd className="font-medium text-foreground">{course.metadata.category}</dd>
              </>
            )}
            {course.metadata.year && (
              <>
                <dt>Year</dt>
                <dd className="font-medium text-foreground">{course.metadata.year}</dd>
              </>
            )}
            {updatedLabel && (
              <>
                <dt>Updated</dt>
                <dd className="font-medium text-foreground">{updatedLabel}</dd>
              </>
            )}
            <dt>Source</dt>
            <dd className="break-all font-medium text-foreground">{course.source}</dd>
            {course.metadata.cta && (
              <>
                <dt>CTA</dt>
                <dd>
                  <a className="inline-flex items-center gap-1 text-primary underline" href={course.metadata.cta} target="_blank" rel="noreferrer">
                    Visit link <ExternalLink className="h-3 w-3" />
                  </a>
                </dd>
              </>
            )}
          </dl>
        </div>
      </CardHeader>
      <CardContent className="space-y-6">
        <section>
          <div className="flex items-center justify-between">
            <h3 className="text-sm font-semibold uppercase tracking-wide text-muted-foreground">Sessions</h3>
            <span className="text-xs text-muted-foreground">{course.sessions.length} items</span>
          </div>
          <ol className="mt-4 space-y-4">
            {course.sessions.map((session, index) => (
              <li key={session.id} className="rounded-xl border border-border bg-card/40 p-4 shadow-sm">
                <div className="flex items-start justify-between gap-4">
                  <div>
                    <p className="text-sm font-semibold text-foreground">
                      {index + 1}. {session.title || session.name}
                    </p>
                    {session.tagline && <p className="text-xs text-muted-foreground">{session.tagline}</p>}
                  </div>
                  {session.rank && (
                    <span className="rounded-full bg-primary/10 px-3 py-0.5 text-xs font-semibold text-primary">
                      Rank {session.rank}
                    </span>
                  )}
                </div>
                {session.description && (
                  <p className="mt-2 text-sm text-muted-foreground">{session.description}</p>
                )}
                {session.keyIdeas?.length ? (
                  <ul className="mt-3 list-disc space-y-1 pl-5 text-sm text-muted-foreground">
                    {session.keyIdeas.map((idea, ideaIndex) => (
                      <li key={`${session.id}-${ideaIndex}`}>{idea}</li>
                    ))}
                  </ul>
                ) : null}
                {session.callToAction && (
                  <a
                    href={session.callToAction}
                    className="mt-3 inline-flex items-center gap-1 text-xs font-semibold text-primary hover:underline"
                    target="_blank"
                    rel="noreferrer"
                  >
                    Explore resources <ExternalLink className="h-3 w-3" />
                  </a>
                )}
              </li>
            ))}
          </ol>
        </section>
      </CardContent>
    </Card>
  );
}
