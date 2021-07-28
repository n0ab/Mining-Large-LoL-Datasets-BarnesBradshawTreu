# Mining-Large-LoL-Datasets-BarnesBradshawTreu
Repository for "Mining Large League of Legends Datasets in Parallel"

This repository contains relevant Python scripts and datasets used for this project.

**INCLUDED DATA**
drive-download-20210728T174440Z-001
drive-download-20210728T174641Z-001
SM_AGGREGATE_NOSPACE
champdataverbose

**INCLUDED SCRIPTS**
SimilarChamps
  -SimilarChamps was our baseline similarity script for champions
APIGrabber
  -Sample grabber that leverages Riot API
summonerID
  -API script which retrieves summoner (player) IDs
summonerIDjaccard
  -variation on summonerID that uses jaccard similarity metric
summonerIDeuclidean
  -variation on summonerID that uses euclidean similarity metric
fuzzyChampSimilarity
  -champion similarity which uses a "fuzzy" similarity metric
KNNchampdata
  -initial KNN algorithm using a less verbose dataset
KNNverbosemapreduce
  -Map reduced version of our KNN algorithm which uses the homemade dataset (champdataverbose)
matchWinLossAPI
  -API grabber which grabs matches, the champions in them, and if the team won or not
KNNTest
  -test script for initial KNN script
KNNplus1steroid
  -Steroided version of our KNN algorithm
HardestArchetype
  -Test file which generates the "hardest" archetype
LoLbans
KNNmr
MovieSimilarities
