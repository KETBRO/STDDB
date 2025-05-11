import re
import pubchempy as pcp

def get_cas_numbers_from_cids(cids):
    cas_rns = []
    for cid in cids:
        compound = pcp.Compound.from_cid(cid)
        if compound.synonyms:
            for syn in compound.synonyms:
                match = re.match(r'(\d{2,7}-\d\d-\d)', syn)
                if match:
                    cas_rns.append(match.group(1))
    return cas_rns

# Example usage:
cids = [5793]  # Replace these with the CIDs you want to fetch
cas_numbers = get_cas_numbers_from_cids(cids)
print("CAS numbers:", cas_numbers)
