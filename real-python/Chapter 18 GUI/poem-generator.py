import tkinter as tk
import random
from tkinter.filedialog import asksaveasfilename
from tkinter.constants import GROOVE


def poem_generation():
    # Delete every spaced characters in the entry and make the entry a list.

    nouns = ent_nouns.get()
    nouns = " ".join(nouns.strip(',').split()).split(' ')
    nouns = random.sample(nouns, len(nouns))
    if len(nouns) != len(set(nouns)):
        lbl_poem_title["text"] = "Error"
        lbl_poem_line1["text"] = "Please don't enter the same words in each entry."
        return

    verbs = ent_verb.get()
    verbs = " ".join(verbs.strip(',').split()).split(' ')
    verbs = random.sample(verbs, len(verbs))
    if len(verbs) != len(set(verbs)):
        lbl_poem_title["text"] = "Error"
        lbl_poem_line1["text"] = "Please don't enter the same words in each entry."
        return

    adjs = ent_adj.get()
    adjs = " ".join(adjs.strip(',').split()).split(' ')
    adjs = random.sample(adjs, len(adjs))
    if len(adjs) != len(set(adjs)):
        lbl_poem_title["text"] = "Error"
        lbl_poem_line1["text"] = "Please don't enter the same words in each entry."
        return

    preps = ent_prep.get()
    preps = " ".join(preps.strip(',').split()).split(' ')
    preps = random.sample(preps, len(preps))
    if len(preps) != len(set(preps)):
        lbl_poem_title["text"] = "Error"
        lbl_poem_line1["text"] = "Please don't enter the same words in each entry."
        return

    advs = ent_adv.get()
    advs = " ".join(advs.strip(',').split()).split(' ')
    if len(advs) != len(set(advs)):
        lbl_poem_title["text"] = "Error"
        lbl_poem_line1["text"] = "Please don't enter the same words in each entry."
        return

    words_list = [nouns, verbs, adjs, preps, advs]

    try:
        # Poem Title
        if adjs[0][0] in 'ueoai':
            lbl_poem_title["text"] = f"An {adjs[0]} {nouns[0]}".replace(
                ',', '')
        else:
            lbl_poem_title["text"] = f"A {adjs[0]} {nouns[0]}".replace(',', '')

    # Poem line 1

        if adjs[0][0] in 'ueoai':
            lbl_poem_line1["text"] = f"An {adjs[0]} {nouns[0]} {verbs[0]} {preps[0]} the {adjs[1]} {nouns[1]}".replace(
                ',', '')
        else:
            lbl_poem_line1["text"] = f"A {adjs[0]} {nouns[0]} {verbs[0]} {preps[0]} the {adjs[1]} {nouns[1]}".replace(
                ',', '')

    # Poem line 2
        lbl_poem_line2["text"] = f"{advs[0]}, the {nouns[0]} {verbs[1]}".replace(
            ',', '')

    # Poem line 3
        if adjs[2][0] in 'ueoai':
            lbl_poem_line3["text"] = f"the {nouns[1]} {verbs[2]} {preps[2]} an {adjs[2]} {nouns[2]}".replace(
                ',', '')
        else:
            lbl_poem_line3["text"] = f"the {nouns[1]} {verbs[2]} {preps[2]} a {adjs[2]} {nouns[2]}".replace(
                ',', '')

    except IndexError:
        # Check for words
        for lst in words_list:
            if (lst == preps) and (len(lst) < 1):
                lbl_poem_title["text"] = "Error"
                lbl_poem_line1["text"] = "Please enter at least 1 adverb"
            if (lst is not preps) and (len(lst) < 3):
                lbl_poem_title["text"] = "Error"
                lbl_poem_line1["text"] = "Please enter enough words."
                lbl_poem_line2["text"] = "At least 3 words for verbs, nouns, adjectives, prepositions"


def save_poem():
    file_path = asksaveasfilename(filetypes=(
        ('text files', '*.txt'), ('All files', '*.*')))

    if not file_path:
        return
    with open(file_path + ".txt", "w") as ouput_file:
        ouput_file.write(lbl_poem_title["text"])
        ouput_file.write("\n")
        ouput_file.write("\n")
        ouput_file.write(lbl_poem_line1["text"])
        ouput_file.write("\n")
        ouput_file.write(lbl_poem_line2["text"])
        ouput_file.write("\n")
        ouput_file.write(lbl_poem_line3["text"])
        ouput_file.write("\n")


window = tk.Tk()
window.title("Poem Generator")
window.rowconfigure([1], minsize=100, weight=1)

# Body
lbl_instr = tk.Label(
    master=window, text="Enter you favorite words, seperated by commas (1 words for Adverbs and 3 words for others).")
frm_words = tk.Frame(master=window)

lbl_nouns = tk.Label(master=frm_words, text="Nouns:")
ent_nouns = tk.Entry(master=frm_words, width=75)

lbl_verb = tk.Label(master=frm_words, text="Verb:")
ent_verb = tk.Entry(master=frm_words, width=75)

lbl_adj = tk.Label(master=frm_words, text="Adjectives:")
ent_adj = tk.Entry(master=frm_words, width=75)

lbl_prep = tk.Label(master=frm_words, text="Prepositions:")
ent_prep = tk.Entry(master=frm_words, width=75)

lbl_adv = tk.Label(master=frm_words, text="Adverbs:")
ent_adv = tk.Entry(master=frm_words, width=75)

btn_generate = tk.Button(
    master=window, text="Generate", command=poem_generation)


frm_output = tk.Frame(master=window, relief=GROOVE, borderwidth=5)
frm_output.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
frm_output.columnconfigure(0, weight=1)
lbl_your_poem = tk.Label(master=frm_output, text="Your poems:")
lbl_poem_title = tk.Label(master=frm_output, text="")
lbl_poem_line1 = tk.Label(master=frm_output, text="")
lbl_poem_line2 = tk.Label(master=frm_output, text="")
lbl_poem_line3 = tk.Label(master=frm_output, text="")
btn_save_to_file = tk.Button(
    master=frm_output, text="Save to file", command=save_poem)

# Grriding
lbl_instr.grid(column=0, row=0, padx=5, pady=5)

frm_words.grid(column=0, row=1, sticky="ns")
lbl_nouns.grid(column=0, row=0, sticky=tk.E)
ent_nouns.grid(column=1, row=0, sticky="w")
lbl_verb.grid(column=0, row=1, sticky="e")
ent_verb.grid(column=1, row=1, sticky="w")
lbl_adj.grid(column=0, row=2, sticky="e")
ent_adj.grid(column=1, row=2, sticky="w")
lbl_prep.grid(column=0, row=3, sticky="e")
ent_prep.grid(column=1, row=3, sticky="w")
lbl_adv.grid(column=0, row=4, sticky="e")
ent_adv.grid(column=1, row=4, sticky="w")


btn_generate.grid(column=0, row=2, pady=10)

frm_output.grid(column=0, row=3, sticky="nsew", pady=5, padx=5)
lbl_your_poem.grid(column=0, row=0, pady=10, sticky="nsew")
lbl_poem_title.grid(column=0, row=1, pady=10, sticky="ew")
lbl_poem_line1.grid(column=0, row=2, sticky="ew")
lbl_poem_line2.grid(column=0, row=3, sticky="ew")
lbl_poem_line3.grid(column=0, row=4, sticky="ew")
btn_save_to_file.grid(column=0, row=5, padx=10, pady=10)

window.mainloop()
