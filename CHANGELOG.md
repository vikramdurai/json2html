# Changelog

## v1
* Added a function `compile2html` which transforms JSON into HTML.

## v2
* Simplified the code a bit by adding 2 new functions, `processNode` and 
`typicalProcessingOfJSON`, which both do what they say on the tin.

## v3
* Added tests
* Now `compile2html` escapes the data, e.g `<p>a < d</p>` will compile
* into `<p>a &lt; d</p>`.