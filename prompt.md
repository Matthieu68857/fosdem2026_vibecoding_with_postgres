Currently, the app has a single search bar that performs a standard full-text search on the description in my Postgres database.

I want to introduce a more intelligent, AI-powered semantic search using vector embeddings, while still giving users the
option to use the classic search.

Here are the key requirements:

  1. Dual Search Modes: The application should support both the existing "Classic" full-text search and a new "AI" vector search.

  2. User Interface:
      * On the search page, there is a toggle switch with "Classic" and "AI" options. Please make this switch fully functional.
      * The selected search mode should be visually clear to the user (e.g., by highlighting the active option).
      * The user's selection should determine which search logic is executed when they submit a query.

  3. Backend Logic:
      * The backend API should handle requests from the frontend and execute the correct search query based on the mode selected by the user.

  4. Database Preparation:
      * My PostgreSQL database needs to be prepared for vector search. This includes:
          * Ensuring a vector column exists on the products table.
          * Populating that column by generating embeddings from the product descriptions.
          * Making sure the vector column is properly indexed for efficient similarity searches.

Based on what you can observe from the code and database, provide first an implementation plan for these changes to provide a seamless dual-search experience for my users.

Don't perform tests, I'll do them manually.