# Assignment: Data Science Scenarios

In this first assignment, we ask you to think about some real-life process or problem in different problem domains, and how you can improve it using the Data Science process. Think about the following:

1. Which data can you collect?
1. How would you collect it?
1. How would you store the data? How large the data is likely to be?
1. Which insights you might be able to get from this data? Which decisions we would be able to take based on the data?

Try to think about 3 different problems/processes and describe each of the points above for each problem domain.

Here are some of the problem domains and problems that can get you started thinking:

1. How can you use data to improve education process for children in schools?
1. How can you use data to control vaccination during the pandemic?
1. How can you use data to make sure you are being productive at work?
## Instructions

Fill in the following table (substitute suggested problem domains for your own ones if needed):

Example:

| Problem Domain | Problem | Which data to collect | How to store the data | Which insights/decisions we can make | 
|----------------|---------|-----------------------|-----------------------|--------------------------------------|
| Education | In university, we typically have low attendance to lectures, and we have the hypothesis that students who attend lectures on average to better during exams. We want to stimulate attendance and test the hypothesis. | We can track attendance through pictures taken by the security camera in class, or by tracking bluetooth/wifi addresses of student mobile phones in class. Exam data is already available in the university database. | In case we track security camera images - we need to store a few (5-10) photographs during class (unstructured data), and then use AI to identify faces of students (convert data to structured form). | We can compute average attendance data for each student, and see if there is any correlation with exam grades. We will talk more about correlation in [probability and statistics](../../04-stats-and-probability/README.md) section. In order to stimulate student attendance, we can publish the weekly attendance rating on school portal, and draw prizes among those with highest attendance. |

I used ChatGPT to analyze this example. This is a data science thinking exercise, not a technical one.

It is important to:
- Turn a **real-world problem** into a **data problem**
- Think about **data collection -> storage -> analysis -> decision**
- Show awareness of data types, feasibility and ethics

How to read the table:
1. Problem domain: Education

This is for the context. Keep it broad, for example: healthcare, finance, marketing, transportation, education, etc.

2. Problem: Low attendance, hypothesis that attendance improves exam results

This is the core. We have to clarify (1) a problem (e.g. low attendance), (2) a testable hypothesis (attendance <-> exam performance) and (3) a goal (stimulate attendance + test hypothesis). Avoid something vague like "improve education quality", good problems are `specific`, `measurable` and `answerable with data`.

3. Which data to collect: Attendance + exam results

We need to identify:

i) What
- input variables (attendance)
- output/target (exam grades)

ii) How
- multiple data collection methods
- which data is realistic to collect

4. How to store the data: Unstructured images -> AI -> structured data

We think about:
- Data types:
    - Structured (tables, rows, columns)
    - Unstructured (images, text, video)
- Data pipeline

5. Which insights/decisions we can make: correlation + intervention (attendance ranking, prizes)

This is the most important column.

Our analysis must end with:
- **Insights** (what we learn)
- **Actions** (what decisions we make)

🔑 Data is useless unless it changes decisions.

---

After considering all of these objectives, I complete this assignment table:

### Iteration 01

| Problem Domain | Problem | Which data to collect | How to store the data | Which insights/decisions we can make | 
|----------------|---------|-----------------------|-----------------------|--------------------------------------|
| Maps & Exploration | I have a hobby, which is try new places (restaurant, historical places, landscape, entertaining, etc.). However, I do not have much money and time to try them all, so I have to surf the google map to find potential ones. To save time finding these, I want to automate the process of selection by using my past reviews on google maps (there are so many), and test whether there is any correlation between the metadata of the place (introduction, area, menu, pricing range, number of visitors, average rating, etc.) with the possibility I will like it, and predict places I would like through reviews of others | crawl data from google map: My past reviews (ratings, text, etc.), metadata of places (as above); Reviews & Ratings from other users. Context data (time visited, companions, purpose) might be useful but unavailable (if I want I have to annotate them myself but it would answer another problem: does my context of visiting affect my experience) | Ratings and data could be stored in CSV. With text reviews, we can use keyword extraction or vector embeddings. If we want to explore the menu of the restaurants/cafes (unstructured), we might have to do some OCR to discover text-based information, or use AI to summarize its style as text | Recommend new place I'm likely to enjoy, Identify patterns (I like cheap places vs. fancy, quiet vs. crowded) and Discover factors influencing my ratings|

Review from ChatGPT:
- Overall assessment: 8.5/10
- What is good:
    - Clear personal motivation (realistic,grounded)
    - Proper hypothesis-driven thinking
    - End-to-end pipeline is present
    - Excellent awareness of structured vs unstructured data
    - Even think about contextual confounders 
- What to improve:
    - Problem statement is a bit long and unfocused
    - Data collection scope is slightly too anbiguous
    - Insight/decision column can be more decision-oriented


### Iteration 02

| Problem Domain | Problem | Which data to collect | How to store the data | Which insights/decisions we can make | 
|----------------|---------|-----------------------|-----------------------|--------------------------------------|
| Maps & Exploration | I want to efficiently identify new places on Google Maps that I am likely to enjoy, given limited time and budget. I hypothesize that my past ratings correlate with certain place metadata and review characteristics. | My past Google Maps reviews and ratings; place metadata (category, price range, location, popularity, average rating, menu, etc.), and reviews/ratings from other users. Optional self-annotated context data (time visited, companions, purpose, source) could be added later. | Ratings and metadata stored in structured format (CSV). Review text stored as keyword-extracted text or embeddings. Optional OCR or AI summarization for menus if needed to extract textual features | Identify personal preference patterns (e.g., price sensitivity, crowd tolerance), predict and rank places I am likely to enjoy. Reduce time spent manually searching on Google Maps. |

## Rubric

Exemplary | Adequate | Needs Improvement
--- | --- | -- |
One was able to identify reasonable data sources, ways of storing data and possible decisions/insights for all problem domains | Some of the aspects of the solution are not detailed, data storage is not discussed, at least 2 problem domains are described | Only parts of the data solution are described, only one problem domain is considered.
