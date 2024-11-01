
const chet = {
    fg: .586 * 5.8,
    ft: .696,
    threes: 1.5,
    reb: 11.0,
    ast: 2.8,
    stl: 1.5,
    blk: 3.5,
    pts: 22.5
}

const jaylen = {
    fg: .396,
    ft: .784 * 7.4,
    threes: 2.4,
    reb: 7.4,
    ast: 3.6,
    stl: 1.6,
    blk: 0.4,
    pts: 25.8
}

const giannis = {
    fg: .613,
    ft: .551 * 9.8,
    threes: 0.0,
    reb: 10.4,
    ast: 5.2,
    stl: 0.2,
    blk: 0.6,
    pts: 23.8
}

const klay = {
    fg: .451,
    ft: 1 * 0.8,
    threes: 4.3,
    reb: 3.5,
    ast: 1.3,
    stl: 1.3,
    blk: 0.0,
    pts: 16.5
}

const woody = [giannis, klay]
const bruno = [chet, jaylen]

// Function to calculate averages for a team
function calculateTeamAverages(team) {
    // Initialize an object to store the sums
    const sums = {
        fg: 0,
        ft: 0,
        threes: 0,
        reb: 0,
        ast: 0,
        stl: 0,
        blk: 0,
        pts: 0
    };
    
    // Add up all stats
    team.forEach(player => {
        for (const stat in sums) {
            sums[stat] += player[stat];
        }
    });
    
    // Calculate averages
    const averages = {};
    for (const stat in sums) {
        averages[stat] = (sums[stat] / team.length).toFixed(2);
    }
    
    return averages;
}

// Calculate averages for both managers
const woodyAverages = calculateTeamAverages(woody);
const brunoAverages = calculateTeamAverages(bruno);

// Display results
console.log('Woody Team Averages:', woodyAverages);
console.log('Bruno Team Averages:', brunoAverages);