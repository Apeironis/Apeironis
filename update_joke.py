import random
import re

jokes = [
    "Q: How does a bioinformatician spend their vacation?<br>A: Running a clustering analysis on the beach.",
    "Q: What did the DNA say to the other DNA?<br>A: Do these genes make me look fat?",
    "Q: Why don't plants get colds?<br>A: Because they always stay \"green\".",
    "Q: How many bioinformaticians does it take to change a light bulb?<br>A: None – they just do an enrichment analysis on the darkness.",
    "Q: Why did the bioinformatician cross the road twice?<br>A: Once forward and once reverse complement!",
    "Q: Why is the grad student's lab always freezing?<br>A: Because it's full of \"zero citations\".",
    "Q: How to make a grad student shiver in one second?<br>A: Whisper: \"Your file is not saved.\"",
    "Q: Why are gene annotators so lonely?<br>A: Because they always work alone (own).",
    "Q: Why did the bioinformatician break up with their laptop?<br>A: It took up too much space on the desk.",
    "Q: What did the plant do when it saw the window?<br>A: It waved.",
    "Q: Why did DNA go dancing?<br>A: Because it had good genes (jeans).",
    "Q: Why do bioinformaticians love the dark?<br>A: Because their data is always on Illumina.",
    "Q: Why did the sequencer break up with the PCR?<br>A: Because it couldn't handle the amplification of feelings.",
    "Q: What do you call a sequencing run that fails miserably?<br>A: A bad read – and it's not even a good story.",
    "Q: Why are bioinformaticians so bad at dating?<br>A: Because they always get too many mismatches and can never find the right pair.",
    "Q: What did the FASTQ file say to the reference genome?<br>A: “You complete me... but I still have 5% unmapped.”",
    "Q: Why did the bioinformatician bring a ladder to work?<br>A: To climb the coverage mountain.",
    "Q: Why did the bioinformatician break up with their partner?<br>A: Because they couldn't handle the pair‑end reads – they always wanted single‑end.",
    "Q: What did the contig say when it was finally assembled?<br>A: \"I finally feel complete, but I still have gaps.\"",
    "Q: Why do bioinformaticians love the command line?<br>A: Because they can `grep` for love, but they always get `no such file or directory`.",
    "Q: Why was the VCF file always anxious?<br>A: Because it had too many variants and couldn't decide which one was pathogenic.",
    "Q: What's a bioinformatician's favorite dance?<br>A: The SAM‑samba, because it's always ready to be converted to BAM.",
    "Q: Why did the reference genome break up with the query sequence?<br>A: Because the query was too fragmented and had too many gaps.",
]

'''
度假：聚类分析在海滩
DNA对话：基因显胖吗
植物不感冒：保持绿色
换灯泡：富集分析黑暗
过马路两次：正向反向互补
冷实验室：零引用
研究生战栗：文件未保存
基因注释员孤独：own/alone
分手笔记本：占地方
植物挥手：wave
DNA跳舞：基因/牛仔裤
12.喜欢黑暗：Illumina
测序仪与PCR分手：amplification of feelings
失败测序：bad read
生信人约会：mismatches/pair
FASTQ对参考基因组：5% unmapped
17.带梯子：coverage mountain
双端测序 vs 单端
组装完的 contig 仍有 gaps
命令行找爱情
VCF 文件的焦虑
生信人的最爱舞蹈
23.参考基因组与 query 分手
'''

def update_readme():
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("README.md not found. Make sure you're in the repo root.")
        return

    joke_text = random.choice(jokes)
    new_block = f'<!-- BIO_JOKE_START -->\n<p align="center">\n  {joke_text}\n</p>\n<!-- BIO_JOKE_END -->'

    pattern = r'<!-- BIO_JOKE_START -->.*?<!-- BIO_JOKE_END -->'
    new_content = re.sub(pattern, new_block, content, flags=re.DOTALL)

    if new_content == content:
        print("Could not find <!-- BIO_JOKE_START --> and <!-- BIO_JOKE_END --> markers in README.md.")
        return

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("Biology joke updated!")
    print(f"Today's joke: {joke_text}")

if __name__ == "__main__":
    update_readme()