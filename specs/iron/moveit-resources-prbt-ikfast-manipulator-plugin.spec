# Meta Package
Name:           ros-iron-moveit-resources-prbt-ikfast-manipulator-plugin
Version:        2.8.0
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-iron-moveit_resources_prbt_ikfast_manipulator_plugin and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-moveit_resources_prbt_ikfast_manipulator_plugin
Requires:       ros2-iron-moveit_resources_prbt_ikfast_manipulator_plugin-devel

Obsoletes: ros-iron-moveit-resources-prbt-ikfast-manipulator-plugin < 2.8.0-1

%description
The prbt_ikfast_manipulator_plugin package

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.8.0-1
- Update to latest release
