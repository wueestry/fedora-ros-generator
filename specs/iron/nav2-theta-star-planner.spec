# Meta Package
Name:           ros-iron-nav2-theta-star-planner
Version:        1.2.7
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-nav2_theta_star_planner and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-nav2_theta_star_planner
Requires:       ros2-iron-nav2_theta_star_planner-devel

Obsoletes: ros-iron-nav2-theta-star-planner < 1.2.7-1

%description
Theta* Global Planning Plugin

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.7-1
- Update to latest release
