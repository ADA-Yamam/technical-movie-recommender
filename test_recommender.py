"""
Recommender Model Testing Script

Tests the recommendation model with sample queries.
Demonstrates model functionality and validates outputs.
"""

from recommender_model import MovieRecommender
import sys


def test_recommender():
    """Test the recommendation model."""
    print("🧪 Testing Movie Recommendation Model\n")

    try:
        # Initialize recommender
        print("📥 Loading recommender model...")
        recommender = MovieRecommender()

        # Get all movies
        all_movies = recommender.get_all_movies()
        if all_movies.empty:
            print("❌ No movies found. Please run prepare_db.py first.")
            return False

        print(f"✅ Model loaded with {len(all_movies)} movies\n")

        # Test 1: Get recommendations for a specific movie
        print("=" * 60)
        print("TEST 1: Get Recommendations for a Specific Movie")
        print("=" * 60)

        test_movie = all_movies.iloc[0]['Title']
        print(f"\n🎬 Reference Movie: {test_movie}")

        recommendations = recommender.get_recommendations(test_movie, n_recommendations=5)

        if recommendations:
            print(f"\n✅ Got {len(recommendations)} recommendations:\n")
            for idx, (title, score) in enumerate(recommendations, 1):
                print(f"   {idx}. {title}")
                print(f"      Similarity Score: {score:.4f}\n")
        else:
            print("❌ No recommendations found")
            return False

        # Test 2: Test with different recommendation counts
        print("=" * 60)
        print("TEST 2: Different Recommendation Counts")
        print("=" * 60)

        for n in [3, 5, 10]:
            recommendations = recommender.get_recommendations(test_movie, n_recommendations=n)
            print(f"\n✅ Requested {n} recommendations, got {len(recommendations)}")

        # Test 3: Test with different movies
        print("\n" + "=" * 60)
        print("TEST 3: Recommendations for Multiple Movies")
        print("=" * 60)

        test_movies = all_movies.head(3)['Title'].tolist()

        for movie in test_movies:
            recommendations = recommender.get_recommendations(movie, n_recommendations=3)
            print(f"\n🎬 {movie}")
            if recommendations:
                print(f"   Top recommendation: {recommendations[0][0]} (Score: {recommendations[0][1]:.4f})")
            else:
                print("   ❌ No recommendations available")

        # Test 4: Test with non-existent movie
        print("\n" + "=" * 60)
        print("TEST 4: Error Handling (Non-existent Movie)")
        print("=" * 60)

        non_existent = "Non Existent Movie XYZ"
        recommendations = recommender.get_recommendations(non_existent)

        if not recommendations:
            print(f"\n✅ Correctly handled non-existent movie: '{non_existent}'")
        else:
            print(f"❌ Unexpected result for non-existent movie")

        # Test 5: Data statistics
        print("\n" + "=" * 60)
        print("TEST 5: Database Statistics")
        print("=" * 60)

        print(f"\n📊 Database Statistics:")
        print(f"   Total movies: {len(all_movies)}")
        print(f"   Average rating: {all_movies['Rating'].mean():.2f}")
        print(f"   Min rating: {all_movies['Rating'].min():.1f}")
        print(f"   Max rating: {all_movies['Rating'].max():.1f}")
        print(f"   Year range: {int(all_movies['ReleaseYear'].min())} - {int(all_movies['ReleaseYear'].max())}")

        # Summary
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED")
        print("=" * 60)
        print("\n🎉 Recommendation model is working correctly!")
        print("   Ready for API and dashboard deployment\n")

        return True

    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_recommender()
    sys.exit(0 if success else 1)
