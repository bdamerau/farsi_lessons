import polars as pl

class PracticeSet:
    def __init__(self,dictfile):
        PracticeSet.dictionary = pl.read_csv(dictfile)
    
    def practice(self):
        print('What would you like to practice?\n')
        print('Categories')
        print('----------')
        group = input(", ".join(practice_groups)+"\n")
        if group.lower()=='verbs':
            practice_df = self.dictionary.filter(
                pl.col('Part of Speech')=='verb'
            )
        elif group.lower() == 'all':
            practice_df=self.dictionary
        else:
            practice_df=self.dictionary.filter(
                pl.col('Category')==group.lower()
            )
        #start the practice
        end = False
        while not end:
            sample_df = practice_df.sample(1)
            farsi_input = input(f'{sample_df['Word'][0]} - ')
            if farsi_input=='end':
                end=True
            else:
                print(f'{sample_df['Farsi'][0]}\n')
                practice_df=practice_df.filter(pl.col('Word')!=sample_df['Word'][0])
                if len(practice_df)==0:
                    end = True
                    print('All Words Reviewed!')

ps = PracticeSet('../dictionary/dictionary.csv')
practice_groups = ps.dictionary['Category'].drop_nulls().unique().to_list()+['verbs','all']

print('Let\'s Learn!\n')
end = False
while not end:
    ps.practice()
    continue_practice = input('Would you like to continue? (y/n)')
    if continue_practice.lower()=='n':
        end = True
print('All Done!')
