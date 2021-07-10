git tag -a $(cat VERSION) -m 'Release v$(cat VERSION)'
git push --tags
