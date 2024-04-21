json.extract! post, :id, :title, :author, :description, :note, :created_at, :updated_at
json.url post_url(post, format: :json)
