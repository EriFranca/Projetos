class Post < ApplicationRecord
    validates :title, :author, :description, :note, presence: true
end
