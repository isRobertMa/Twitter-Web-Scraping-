# Load libraries
# jsonlite for dealing with json data, and dplyr for grammar of data manipulation
library(jsonlite)
library(ggplot2)
# Store data from both json file 
follow.data <- fromJSON("C:\\Users\\hansh\\Downloads\\following.json")
engage.data <- fromJSON("C:\\Users\\hansh\\Downloads\\engagement.json")
# Obtain names 
names(follow.data)
names(engage.data)

# Function for task3 Network Overlap 
# Takes any two influencers' user ID's and calculate the fraction of
# followers these two influencers share over the total number of followers of the less followed influencer.
network_overlap <- function(influencer_uid1, influencer_uid2, jsondata){
  
  # Create subsets of followers of provided influencers 
  uid1_followers <- jsondata$follower_uid[jsondata$influencer_uid == influencer_uid1]
  uid2_followers <- jsondata$follower_uid[jsondata$influencer_uid == influencer_uid2]
  
  # Get the shared followers between two influencers
  shared_followers <- intersect(uid1_followers, uid2_followers)
  # Calculate the total amount of shared followers
  shared_total <- length(shared_followers)
  # Store respective length of provided influencers
  n1 <- length(uid1_followers)
  n2 <- length(uid2_followers)
  # ifelse expression return whichever uid have lesser followers
  lesser_uid <- ifelse(n1 <= n2, n1, n2)
  
  # Calculate the total fraction 
  return(shared_total/lesser_uid)
  }
result1 <- network_overlap("21722318", "27801361", follow.data)
result1

# Functrion for task3 Engagement overlap 
# Takes any two influencers' user ID's and calculate the fraction of engagers of
# these two influencers' tweets as a function of the total number of engagers of 
# the less engaged influencer.
engagement_overlap <- function(influencer_uid1, influencer_uid2, jsondata){
  
  # Create subsets of followers of provided influencers 
  uid1_followers <- jsondata$follower_uid[jsondata$influencer_uid == influencer_uid1]
  uid2_followers <- jsondata$follower_uid[jsondata$influencer_uid == influencer_uid2]
  
  # Get the shared engagers between two influencers
  shared_followers <- intersect(uid1_followers, uid2_followers)
  # Calculate the total amount of shared engagers
  shared_total <- length(shared_followers)
  # Store respective length of provided influencers
  n1 <- length(uid1_followers)
  n2 <- length(uid2_followers)
  # ifelse expression return whichever uid have lesser engagers
  lesser_uid <- ifelse(n1 <= n2, n1, n2)
  
  # Calculate the total fraction 
  return(shared_total/lesser_uid)
}
result2 <- engagement_overlap("21722318", "27801361", engage.data)
result2

create_hist <- function(engagement_json, following_json){
  # Create two empty vectors one for engagement and one for network
  engage_fracs <- c()
  follow_fracs <- c()
  # Extract unique influencer_id
  uids <- unique(following_json$follower_uid)
  
  # Double for loop interate through all pairs of influencers 
  for (i in 1:(length(uids) - 1)){
    for (j in (i+1): length(uids)){
      # Influencers pair 
      influencer1 <- uids[i]
      influencer2 <- uids[j]
      
      # Obtain an single engager overlap fraction 
      engage_frac <- engagement_overlap(influencer1, influencer2, engagement_json)
      # Store the value in fractions vector
      engage_fracs <- c(engage_fracs, engage_frac)   
      # Obtain an single network overlap fraction 
      follow_frac <- network_overlap(influencer1, influencer2, following_json)
      # Store the value in fractions vector
      follow_fracs <- c(follow_fracs, follow_frac)
      }
  }
  # Create historgrams
  # Create histograms
  engager_hist <- ggplot(data.frame(engage_fracs), aes(x = engage_fracs)) +
    geom_histogram(binwidth = 0.1, fill = "blue", color = "black") +
    labs(title = "Engager Fraction Histogram", x = "Engager Fraction", y = "Count")
  
  follower_hist <- ggplot(data.frame(follow_fracs), aes(x = follow_fracs)) +
    geom_histogram(binwidth = 0.1, fill = "green", color = "black") +
    labs(title = "Follower Fraction Histogram", x = "Follower Fraction", y = "Count")
  
  # Save histograms as PNG files
  ggsave("engager_histogram.png", plot = engager_hist)
  ggsave("follower_histogram.png", plot = follower_hist)
}
create_hist(engage.data, follow.data)
