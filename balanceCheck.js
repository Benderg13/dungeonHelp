//User should start the program with the 6 stat valued after the command seperated by a space
//like node balanceCheck.js 16 12 16 11 12 9
var stats=process.argv.slice(2,8);
var point_buy = [-9, -6, -4, -2, -1, 0, 1, 2, 3, 4, 5, 7, 9, 12, 15, 19];
var point_total = 0;
var arraylength = stats.length;

if(arraylength!=6){
    console.log("Need 6 stats in call");
    return;
}

for(var i = 0;i<arraylength;i++){;
    if(2 < stats[i] && stats[i] < 19){
        point_total += point_buy[stats[i]-3];
    }else{
        console.log("Invalid stat value:" + stats[i]);
        return;
    }
}

console.log("Point total using point buy value:" + point_total);

if (point_total < 18){
    console.log("Reroll stats");
}else if(point_total < 24){
    console.log("Point total low, highly consider rerolling");
}else if(point_total < 27){
    console.log("Below standard distribution, consider rerolling stats");
}else if(point_total > 45){
    console.log("Unusually high stats");
}else{
    console.log('Looks good!');
}