from parsers.sbi_parser import SbiParser

if __name__ == "__main__":
    parser = SbiParser("/home/direwolf05/credit-card-analyser/card_statements/dec_24")
    parser.read_card_statement()
