
-- Query 1: Top 5 Highest-Magnitude Earthquakes
-- Finds the five earthquakes with the largest magnitudes.

SELECT *
FROM earthquakes
WHERE id NOT IN ('test_load_001', 'test_load_002', 'test_load_003')
ORDER BY mag DESC
LIMIT 5;


-- Query 2: Average Earthquake Magnitude
-- Calculates the average magnitude of all real earthquakes,
-- excluding our test records.

SELECT AVG(mag) AS average_mag
FROM earthquakes
WHERE id NOT IN ('test_load_001', 'test_load_002', 'test_load_003');


-- Query 3: Earthquake Count by Magnitude Category
-- Groups earthquakes into Small, Moderate, and Larger categories
-- and counts how many earthquakes belong to each category.

SELECT
    CASE
        WHEN mag < 2.0 THEN 'Small'
        WHEN mag < 4.0 THEN 'Moderate'
        ELSE 'Larger'
    END AS magnitude_category,
    COUNT(*) AS earthquake_count
FROM earthquakes
WHERE id NOT IN ('test_load_001', 'test_load_002', 'test_load_003')
GROUP BY magnitude_category;


-- Query 4: Average Depth by Magnitude Category
-- Calculates the average earthquake depth for each magnitude category.

SELECT
    CASE
        WHEN mag < 2.0 THEN 'Small'
        WHEN mag < 4.0 THEN 'Moderate'
        ELSE 'Larger'
    END AS magnitude_category,
    AVG(depth) AS depth_avg
FROM earthquakes
WHERE id NOT IN ('test_load_001', 'test_load_002', 'test_load_003')
GROUP BY magnitude_category;


-- Query 5: Minimum and Maximum Depth by Magnitude Category
-- Finds the shallowest and deepest earthquakes in each category
-- and counts the total number of earthquakes per category.

SELECT
    CASE
        WHEN mag < 2.0 THEN 'Small'
        WHEN mag < 4.0 THEN 'Moderate'
        ELSE 'Larger'
    END AS magnitude_category,
    MIN(depth) AS min_depth,
    MAX(depth) AS max_depth,
    COUNT(*) AS earthquake_count
FROM earthquakes
WHERE id NOT IN ('test_load_001', 'test_load_002', 'test_load_003')
GROUP BY magnitude_category;


-- Query 6: Negative Earthquake Depth Analysis
-- Counts how many earthquakes have negative depth values
-- within each magnitude category.

SELECT
    CASE
        WHEN mag < 2.0 THEN 'Small'
        WHEN mag < 4.0 THEN 'Moderate'
        ELSE 'Larger'
    END AS magnitude_category,
    COUNT(*) FILTER (WHERE depth < 0) AS negative_earthquake_count
FROM earthquakes
WHERE id NOT IN ('test_load_001', 'test_load_002', 'test_load_003')
GROUP BY magnitude_category;
