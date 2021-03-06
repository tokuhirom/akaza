import logging

from akaza_data_utils import copy_snapshot
from akaza_data_utils import get_sig


def main():
    with open('work/jawiki.wfreq', 'r') as rfp, \
            open('work/jawiki.vocab', 'w') as wfp:
        vocab = []
        for line in rfp:
            m = line.rstrip().split(' ')
            if len(m) == 2:
                word, cnt = m
                if word.endswith('/UNK'):
                    logging.info(f"Skip: {word}(unknown word)")
                elif "\u200f" in line:  # RTL
                    logging.info(f"Skip: {word}(RTL)")
                elif '/' not in word:
                    logging.info(f"Skip: {word}(no slash)")
                elif int(cnt) >= 15 and len(word) > 0:
                    vocab.append(word)
                else:
                    logging.info(f"Skip: {word}: {cnt}(few count)")

        for word in sorted(vocab):
            wfp.write(word + "\n")

    copy_snapshot('work/jawiki.vocab')


if __name__ == '__main__':
    sig = get_sig()
    logging.basicConfig(level=logging.INFO, filename=f"work/dump/{sig}-wfreq2vocab.log")
    main()
