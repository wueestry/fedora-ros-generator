# Meta Package
Name:           ros-humble-ompl
Version:        1.6.0
Release:        1%{?dist}
License:        BSD
URL:            https://ompl.kavrakilab.org
Summary:        Meta package for ros2-humble-ompl and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ompl
Requires:       ros2-humble-ompl-devel

Obsoletes: ros-humble-ompl < 1.6.0-1

%description
OMPL is a free sampling-based motion planning library.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.6.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.6.0-1
- update to latest upstream release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.6.0-1
- Initial humble build
