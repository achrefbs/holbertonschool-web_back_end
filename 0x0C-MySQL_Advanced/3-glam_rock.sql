-- SQL script that lists all bands with Glam rock as their main style

SELECT
  band_name AS band_name,
  IFNULL(split, 2020) - IFNULL(formed, 0) AS lifespan
from
  metal_bands
WHERE
  style LIKE '%Glam rock%'
