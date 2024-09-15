DNA_strand=lambda dna:"".join([dict(zip('ATCG', 'TAGC'))[x] for x in dna])

print(DNA_strand('ATTGC'))