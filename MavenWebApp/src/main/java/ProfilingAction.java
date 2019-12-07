import com.opensymphony.xwork2.Action;

public class ProfilingAction {
	private String data;
	private String team;
	private String support;
	public String getComments() {
		boolean supportsFirstTeam = false;
		if(support.equals("true")) {
			supportsFirstTeam = true;
		}
		data = SemanticWeb.getData(team, supportsFirstTeam);
		return Action.SUCCESS;
	}
	
	public String dispatch() {
		return Action.SUCCESS;
	}
	public String getData() {
		return data;
	}
	public void setData(String data) {
		this.data = data;
	}
	public String getTeam() {
		return team;
	}
	public void setTeam(String team) {
		this.team = team;
	}

	public String getSupport() {
		return support;
	}


	public void setSupport(String support) {
		this.support = support;
	}
}
