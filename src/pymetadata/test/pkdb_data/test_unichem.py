import pytest

from pymetadata.pkdb_data.unichem import UnichemQuery


def test_unichem():
    inchikey = "NGBFQHCMQULJNZ-UHFFFAOYSA-N"
    results = UnichemQuery.query_xrefs(inchikey=inchikey, cache=False)
    results = UnichemQuery.query_xrefs(inchikey=inchikey, cache=True)
