CREATE TABLE music_events.music_events (
  eventID string,
  userID int64,
  userUUID string,
  countryCode string,
  name string,
  artist string,
  timestamp timestamp,
  PublishTime Datetime 
  )
PARTITION BY DATE(timestamp)