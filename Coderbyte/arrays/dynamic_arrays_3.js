// meetings are represented by blocks of 30 minutes
// The first block begins at 9 a.m

let meetings = [
  { startTime: 4, endTime: 8 }, // 11 am - 1pm
  { startTime: 3, endTime: 5 }, // 10:30 am - 11:30 am
  { startTime: 0, endTime: 1 }, // 9 am - 9:30 am
  { startTime: 10, endTime: 12 }, // 2 pm - 3pm
  { startTime: 9, endTime: 10 }, // 1:30 pm - 2pm
];

// return the list of merged times where everyone is free to play games
const findEveryoneFreeTime = (meetings) => {
  meetings.sort((a, b) => a.startTime - b.startTime);

  let merged = [meetings[0]];

  for (let i = 1; i < meetings.length; i++) {
    let lastItemMerged = meetings[merged.length - 1];

    if (lastItemMerged.endTime >= meetings[i].startTime) {
      let lateEndTime =
        lastItemMerged.endTime > meetings[i].endTime
          ? lastItemMerged.endTime
          : meetings[i].endTime;

      merged[merged.length - 1] = {
        startTime: lastItemMerged.startTime,
        endTime: lateEndTime,
      };
      i = i + 1;
      continue;
    }
    merged.push(meetings[i]);
  }

  return merged;
};

console.log(findEveryoneFreeTime(meetings));
