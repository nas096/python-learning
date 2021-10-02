from random import choice,sample

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]

verbs =  ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]

adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]

prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]

adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

vowel = ["u", "e", "o", "a", "i"]

random_nouns = sample(nouns,3)
random_verbs = sample(verbs,3)
random_adj = sample(adjectives, 3)
random_prep = sample(prepositions, 2)
random_adverbs = choice(adverbs)

if random_adj[0][0] in vowel:
    articles = "An"
else:
    articles = "A"

print(f'{articles} {random_adj[0]} {random_nouns[0]}\n')
print(f'{articles} {random_adj[0]} {random_nouns[0]} {random_prep[0]} the {random_adj[1]} {random_nouns[1]} {random_adverbs}, the {random_nouns[0]} {random_verbs[1]}')

print(f"the {random_nouns[1]} {random_verbs[2]} {random_prep[1]} a {random_adj[2]} {random_nouns[2]}")