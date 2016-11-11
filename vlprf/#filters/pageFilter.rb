def pageFilter(adrPageTable)
  if adrPageTable[:kramdown]
    adrPageTable[:bodytext] = Kramdown::Document.new(adrPageTable[:bodytext],
    :auto_ids => false, :entity_output => :numeric).to_html.gsub("&quot;", '"')
    adrPageTable[:bodytext] = adrPageTable[:bodytext].gsub("&lt;%", "<%")
    adrPageTable[:bodytext] = adrPageTable[:bodytext].gsub("%&gt;", "%>")
    adrPageTable[:bodytext] = adrPageTable[:bodytext].gsub("&#8220;", "\"")
    adrPageTable[:bodytext] = adrPageTable[:bodytext].gsub("&#8221;", "\"")
    adrPageTable[:bodytext] = adrPageTable[:bodytext].gsub("=&gt;", "=>")
  end
end

