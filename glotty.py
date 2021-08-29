import sqlglot
import click


DIALECT_PRESTO = 'presto'
DIALECT_SPARK = 'spark'

@click.command()
@click.option('-p2s', 'transformation', required=True, flag_value='p2s', help="Transpile From Presto to Spark")
@click.option('-s2p', 'transformation', required=True, flag_value='s2p', help="Transpile From Spark to Presto")
@click.option('--pretty/--no-pretty', default=False, help="Pretty or simple")
@click.argument('sql', required=True)
def from_this_to_that(sql, transformation, pretty=False):
    '''
        Transpiles SQL from Presto to Spark or vice-versa
        Ex. glotty.py -s2p "select DATE_ADD(date_trunc('week', date(current_timestamp)), -7)"
    '''

    if transformation == 'p2s':
        from_dialect = DIALECT_PRESTO
        to_dialect = DIALECT_SPARK
    else:
        from_dialect = DIALECT_SPARK
        to_dialect = DIALECT_PRESTO

    try:
        out = sqlglot.transpile(sql, read=from_dialect, write=to_dialect, pretty=pretty)[0]
    except:
        out = f"ERROR: some error occurred in transpiling. Are you sure that your SQL is syntactically valid {from_dialect} sql?"

    print(out)

if __name__ == '__main__':
    from_this_to_that()




