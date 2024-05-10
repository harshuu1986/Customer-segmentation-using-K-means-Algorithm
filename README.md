# Customer-segmentation-using-K-means-Algorithm
### What is Customer Segmentation?
<br>
Customer Segmentation is the process of division of customer base into several groups of individuals that share a similarity in different ways that are relevant to marketing such as gender, age, interests, and miscellaneous spending habits.
<br>
<br>
Companies that deploy customer segmentation are under the notion that every customer has different requirements and require a specific marketing effort to address them appropriately. Companies aim to gain a deeper approach of the customer they are targeting. Therefore, their aim has to be specific and should be tailored to address the requirements of each and every individual customer. Furthermore, through the data collected, companies can gain a deeper understanding of customer preferences as well as the requirements for discovering valuable segments that would reap them maximum profit. This way, they can strategize their marketing techniques more efficiently and minimize the possibility of risk to their investment.
<br>
<br>
The technique of customer segmentation is dependent on several key differentiators that divide customers into groups to be targeted. Data related to demographics, geography, economic status as well as behavioral patterns play a crucial role in determining the company direction towards addressing the various segments
<br>

### What is K Means Algorithm? 
<br>
While using the k-means clustering algorithm, the first step is to indicate the number of clusters (k) that we wish to produce in the final output. The algorithm starts by selecting k objects from dataset randomly that will serve as the initial centers for our clusters. These selected objects are the cluster means, also known as centroids. Then, the remaining objects have an assignment of the closest centroid. This centroid is defined by the Euclidean Distance present between the object and the cluster mean. We refer to this step as “cluster assignment”. When the assignment is complete, the algorithm proceeds to calculate new mean value of each cluster present in the data. After the recalculation of the centers, the observations are checked if they are closer to a different cluster. Using the updated cluster mean, the objects undergo reassignment. This goes on repeatedly through several iterations until the cluster assignments stop altering. The clusters that are present in the current iteration are the same as the ones obtained in the previous iteration.
<br>

### Dataset
<br>
The dataset is aquired from kaggle and the link is given below :
<br>
<br>
https://in.docworkspace.com/d/sIHbF-e78Ae-u-LEG
<br>
<br>
The dataset consists of following five features of 850 customers:
<br>
<br>
- CustomerID: Unique ID assigned to the customer.
<br>
<br>
- Age: Divide customers into age.
<br>
<br>
- Income: Process of dividing customers based on their income level.
<br>
<br>
- Card Debt: Debt of the customers.
<br>
<br>
- Debt Income Ratio: Customers are grouped into tiers based on their credit scores.
<br>

### K-means Algorithm
-  We specify the number of clusters that we need to create.
-  The algorithm selects k objects at random from the dataset. This object is the initial cluster or mean.
-  The closest centroid obtains the assignment of a new observation. We base this assignment on the Euclidean Distance between object and the centroid.
-  k clusters in the data points update the centroid through calculation of the new mean values present in all the data points of the cluster. The kth cluster’s centroid has a -  -  Length of p that contains means of all variables for observations in the k-th cluster. We denote the number of variables with p.
-  Iterative minimization of the total within the sum of squares. Then through the iterative minimization of the total sum of the square, the assignment stop wavering when we -  -  Achieve maximum iteration. The default value is 10 that the R software uses for the maximum iterations.
<br>

### Determining Optimal Clusters
While working with clusters, you need to specify the number of clusters to use. You would like to utilize the optimal number of clusters. To help you in determining the optimal clusters, there are three popular methods –<br>

-  Elbow method
The main goal behind cluster partitioning methods like k-means is to define the clusters such that the intra-cluster variation stays minimum.
<br>

### With the help of clustering, we can understand the variables much better, prompting us to take careful decisions. With the identification of customers, companies can release products and services that target customers based on several parameters like income, age, education, card debt, address, debt income ratio etc.
