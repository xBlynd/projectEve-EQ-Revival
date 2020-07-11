function monsterBaseAttackRandom(baseAttackMin, baseAttackMax) {
	return Math.floor(Math.random() * (baseAttackMin - baseAttackMax))
}

console.log(monsterBaseAttackRandom(gameData['monster']['attack_min'], gameData['monster']['attack_max']))
const owner = {
	name: "blynd",
	startingRole: "Game Dev",
	description: "I break a lot."
}

const Warrior = {
	baseHealth: 100,
	baseStamina: 15,
	baseArmor: 17,
	baseAttackMin: 10,
	baseAttackMax: 20
}

const players = {
	startingRole: "Guest",
	playerBaseHealth: 100,
	playerBaseDamage: 11,
	playerBaseStamina: 14,
	playerBaseArmor: 10
}
console.log(owner, players);