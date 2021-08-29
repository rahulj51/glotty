## Glotty

CLI wrapper over [Toby Mao](https://github.com/tobymao)'s [sqlglot](https://github.com/tobymao/sqlglot) library
to transpile SQL between Presto and Spark.

### How to use
```shell
Usage: glotty [OPTIONS] SQL

  Transpiles SQL from Presto to Spark or vice-versa Ex. glotty.py -p2s "select
  DATE_ADD(date_trunc('week', date(current_timestamp)), -7)"

Options:
  -p2s                    Transpile From Presto to Spark  [required]
  -s2p                    Transpile From Spark to Presto  [required]
  --pretty / --no-pretty  Pretty or simple
  --help                  Show this message and exit.
```

### Examples

```shell
    $ glotty.py -s2p "select DATE_ADD(date_trunc('week', date(current_timestamp)), -7)"
    $ python glotty.py -p2s "SELECT DATE_ADD('day', -7, DATE_PARSE(DATE_TRUNC('week', CAST((current_timestamp) AS date)), '%Y-%m-%d'))"
    $ cat mysql.sql | glotty.py -s2p
```

