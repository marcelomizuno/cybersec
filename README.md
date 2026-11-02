# cybersec

Skill para Claude Code com uma base de referência de cibersegurança curada a partir do dataset
[Vyber07/cyber-security](https://huggingface.co/datasets/Vyber07/cyber-security) (Apache-2.0).

Do dataset original (~18 GB) foram aproveitados só os guias estruturados e úteis: playbooks de IR,
queries de threat hunting, padrões de detecção, hardening, pentest web/API, red team, cloud,
containers, forense, criptografia, compliance e segurança IoT Thread/Matter. Ficaram de fora
duplicatas, tarballs do ARVO, cenários sintéticos (`*-realtime-scenarios`, `*-real-examples*`) e
os textos de malware gerados por template a partir do MITRE.

## Estrutura

```
.claude-plugin/          manifesto do plugin + marketplace local
skills/cybersec/         a skill (SKILL.md + references/*.md)
scripts/sources.json     mapeamento arquivo de referência -> arquivos do dataset
scripts/build_references.py  gera references/*.md a partir do dataset
```

## Instalação

Como skill pessoal (symlink):

```bash
ln -s "$PWD/skills/cybersec" ~/.claude/skills/cybersec
```

Ou como plugin:

```
/plugin marketplace add /home/marcelo/projects/cybersec
/plugin install cybersec@cybersec
```

## Regenerar as referências

O dataset é gated: aceite os termos na página do Hugging Face e faça `hf auth login`.

```bash
hf download Vyber07/cyber-security --repo-type dataset --local-dir data/ \
    $(python3 scripts/build_references.py --list)
python3 -I scripts/build_references.py data/
```

Para incluir ou remover conteúdo, edite `scripts/sources.json`.
