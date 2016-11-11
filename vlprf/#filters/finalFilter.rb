def finalFilter(adrPageTable)
  if adrPageTable[:kramdown]
    adrPageTable[:renderedText] = adrPageTable[:renderedText].gsub("><![CDATA", ">%<![CDATA")
    adrPageTable[:renderedText] = adrPageTable[:renderedText].gsub("]]>", "%]]>")
  end
end