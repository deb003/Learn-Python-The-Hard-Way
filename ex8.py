formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type right.",
	"But it didn't sing.", # I think this is coming with double quotes as it has a single quote. Yes. Right.
	"So I said goodnight."
)
