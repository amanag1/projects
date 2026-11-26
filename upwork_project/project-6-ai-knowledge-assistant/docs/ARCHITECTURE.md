# Architecture

1. Local document loader accepts explicitly supported file types.
2. Chunker creates stable passage ordinals tied to source filenames.
3. Retriever ranks passages using a transparent lexical overlap baseline.
4. Answer layer abstains when no evidence is found and returns source passages.
5. CLI presents the answer, source references and review flag.

The lexical retriever is a deliberately transparent baseline, not a claim of semantic search quality. A production extension can replace it with embeddings/vector search while retaining provenance, evidence thresholds and evaluation tests.
