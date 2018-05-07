var scheduler = require('./scheduler.js')
reqListDeadline = [
    {"url": "https://www.google.com", "deadline": 5},
    {"url": "https://www.google.com", "deadline": 4},
    {"url": "https://www.google.com", "deadline": 4},
    {"url": "https://www.google.com", "deadline": 5},
    {"url": "https://www.yahoo.com", "deadline": 6},
    {"url": "https://www.yahoo.com", "deadline": 5},
    {"url": "https://www.yahoo.com", "deadline": 6},
    {"url": "https://www.yahoo.com", "deadline": 5},
    {"url": "https://www.github.com", "deadline": 3},
    {"url": "https://www.github.com", "deadline": 8},
    {"url": "https://www.github.com", "deadline": 8},
    {"url": "https://www.github.com", "deadline": 8},
];

reqListFIFO = [
    {"url": "https://www.google.com", "deadline": 5},
    {"url": "https://www.google.com", "deadline": 4},
    {"url": "https://www.google.com", "deadline": 4},
    {"url": "https://www.google.com", "deadline": 5},
    {"url": "https://www.yahoo.com", "deadline": 6},
    {"url": "https://www.yahoo.com", "deadline": 5},
    {"url": "https://www.yahoo.com", "deadline": 6},
    {"url": "https://www.yahoo.com", "deadline": 5},
    {"url": "https://www.github.com", "deadline": 3},
    {"url": "https://www.github.com", "deadline": 8},
    {"url": "https://www.github.com", "deadline": 8},
    {"url": "https://www.github.com", "deadline": 8},
];

reqListPriority = [
    {"url": "https://www.google.com", "priority": 5},
    {"url": "https://www.google.com", "priority": 4},
    {"url": "https://www.google.com", "priority": 4},
    {"url": "https://www.google.com", "priority": 5},
    {"url": "https://www.yahoo.com", "priority": 6},
    {"url": "https://www.yahoo.com", "priority": 5},
    {"url": "https://www.yahoo.com", "priority": 6},
    {"url": "https://www.yahoo.com", "priority": 5},
    {"url": "https://www.github.com", "priority": 3},
    {"url": "https://www.github.com", "priority": 8},
    {"url": "https://www.github.com", "priority": 8},
    {"url": "https://www.github.com", "priority": 8},
];

console.log(scheduler.sortByDeadline(reqListDeadline));
console.log(scheduler.sortByArrive(reqListFIFO));
console.log(scheduler.sortByPriority(reqListPriority));